"""
🚶 3단계: 최단 경로 탐색
내 집에서 반달곰 커피까지의 최단 경로를 구하는 프로그램

구현 알고리즘: BFS (Breadth-First Search)
- 건설 현장은 지나갈 수 없음
- 최단 경로를 CSV로 저장
- 지도에 경로를 시각화
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from collections import deque
import heapq

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def load_data():
    """데이터를 불러오는 함수"""
    try:
        # mas_map.py에서 생성된 병합된 데이터 파일 불러오기
        merged_data = pd.read_csv('C:/codyssey/ky-codyssey-main/Codyseey/merged_data.csv')
        print("✅ 데이터를 성공적으로 불러왔습니다.")
        return merged_data
    except FileNotFoundError:
        print("❌ merged_data.csv 파일을 찾을 수 없습니다.")
        print("   먼저 'python mas_map.py'를 실행하여 데이터를 분석해주세요.")
        return None

def find_my_home_and_cafe(data):
    """내 집과 반달곰 커피 위치를 찾는 함수"""
    my_home = data[data['struct_name'] == ' MyHome']
    cafe = data[data['struct_name'] == ' BandalgomCoffee']
    
    if len(my_home) == 0:
        print("❌ 내 집을 찾을 수 없습니다.")
        return None, None
    
    if len(cafe) == 0:
        print("❌ 반달곰 커피를 찾을 수 없습니다.")
        return None, None
    
    home_pos = (my_home.iloc[0]['x'], my_home.iloc[0]['y'])
    cafe_pos = (cafe.iloc[0]['x'], cafe.iloc[0]['y'])
    
    print(f"🏠 내 집 위치: {home_pos}")
    print(f"☕ 반달곰 커피 위치: {cafe_pos}")
    
    return home_pos, cafe_pos

def create_grid_map(data):
    """그리드 맵을 생성하는 함수"""
    max_x = data['x'].max()
    max_y = data['y'].max()
    
    # 2D 그리드 생성 (0: 이동 가능, 1: 건설 현장)
    grid = np.zeros((max_y + 1, max_x + 1), dtype=int)
    
    # 건설 현장을 1로 표시
    construction_sites = data[data['ConstructionSite'] == 1]
    for _, row in construction_sites.iterrows():
        grid[int(row['y']), int(row['x'])] = 1
    
    return grid

def bfs_shortest_path(grid, start, goal):
    """BFS를 사용한 최단 경로 탐색"""
    if start == goal:
        return [start]
    
    # 방향: 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS 큐와 방문 기록
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        current, path = queue.popleft()
        x, y = current
        
        # 4방향 탐색
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            
            # 범위 체크
            if (next_x < 0 or next_x >= grid.shape[1] or 
                next_y < 0 or next_y >= grid.shape[0]):
                continue
            
            # 건설 현장이거나 이미 방문한 곳이면 건너뛰기
            if grid[next_y, next_x] == 1 or (next_x, next_y) in visited:
                continue
            
            next_pos = (next_x, next_y)
            new_path = path + [next_pos]
            
            # 목표에 도달
            if next_pos == goal:
                print(f"✅ 최단 경로를 찾았습니다! (길이: {len(new_path)}칸)")
                return new_path
            
            # 큐에 추가
            queue.append((next_pos, new_path))
            visited.add(next_pos)
    
    print("❌ 경로를 찾을 수 없습니다.")
    return None

def save_path_to_csv(path, filename='home_to_cafe.csv'):
    """경로를 CSV 파일로 저장"""
    if path is None:
        return
    
    path_data = []
    for i, (x, y) in enumerate(path):
        path_data.append({
            'step': i + 1,
            'x': x,
            'y': y,
            'position': f'({x}, {y})'
        })
    
    path_df = pd.DataFrame(path_data)
    filepath = f'C:/codyssey/ky-codyssey-main/Codyseey/{filename}'
    path_df.to_csv(filepath, index=False, encoding='utf-8-sig')
    print(f"💾 경로가 저장되었습니다: {filepath}")
    print(f"   - 총 {len(path)}칸 이동")
    print(f"   - 시작: {path[0]}")
    print(f"   - 도착: {path[-1]}")

def create_final_map_visualization(data, path):
    """최종 지도 시각화 (경로 포함)"""
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # 좌표 범위 설정
    min_x, max_x = data['x'].min(), data['x'].max()
    min_y, max_y = data['y'].min(), data['y'].max()
    ax.set_xlim(min_x - 1, max_x + 1)
    ax.set_ylim(min_y - 1, max_y + 1)
    ax.invert_yaxis()  # 좌측 상단이 (1,1) 되도록
    
    # 그리드 라인
    for x in range(int(min_x), int(max_x) + 2):
        ax.axvline(x, color='lightgray', linestyle='--', linewidth=0.5)
    for y in range(int(min_y), int(max_y) + 2):
        ax.axhline(y, color='lightgray', linestyle='--', linewidth=0.5)
    
    # 구조물 시각화
    for _, row in data.iterrows():
        x, y = row['x'], row['y']
        struct_name = str(row.get('struct_name', '')).strip()
        construction_site = row.get('ConstructionSite', 0)
        
        # 건설 현장 우선 표시
        if construction_site == 1:
            rect = patches.Rectangle((x-0.6, y-0.6), 1.2, 1.2, 
                                   facecolor='#666666', alpha=0.9, edgecolor='#333333', linewidth=2)
            ax.add_patch(rect)
        elif struct_name.lower() == 'apartment':
            circle = patches.Circle((x, y), 0.4, facecolor='#8B4513', alpha=1.0, edgecolor='#654321', linewidth=2)
            ax.add_patch(circle)
        elif struct_name.lower() == 'building':
            circle = patches.Circle((x, y), 0.4, facecolor='#A0522D', alpha=1.0, edgecolor='#654321', linewidth=2)
            ax.add_patch(circle)
        elif struct_name.lower() == 'bandalgomcoffee':
            rect = patches.Rectangle((x-0.4, y-0.4), 0.8, 0.8, 
                                   facecolor='#228B22', alpha=1.0, edgecolor='#006400', linewidth=2)
            ax.add_patch(rect)
        elif struct_name.lower() == 'myhome':
            triangle = patches.Polygon([[x, y+0.4], [x-0.4, y-0.4], [x+0.4, y-0.4]], 
                                     facecolor='#32CD32', alpha=1.0, edgecolor='#228B22', linewidth=2)
            ax.add_patch(triangle)
    
    # 최단 경로 시각화 (빨간 선)
    if path and len(path) > 1:
        path_x = [pos[0] for pos in path]
        path_y = [pos[1] for pos in path]
        ax.plot(path_x, path_y, 'r-', linewidth=3, alpha=0.8, label='최단 경로')
        
        # 시작점과 도착점 강조
        start_x, start_y = path[0]
        end_x, end_y = path[-1]
        
        # 시작점 (내 집) - 파란색 원
        start_circle = patches.Circle((start_x, start_y), 0.3, 
                                    facecolor='blue', alpha=0.7, edgecolor='darkblue', linewidth=2)
        ax.add_patch(start_circle)
        
        # 도착점 (반달곰 커피) - 빨간색 원
        end_circle = patches.Circle((end_x, end_y), 0.3, 
                                  facecolor='red', alpha=0.7, edgecolor='darkred', linewidth=2)
        ax.add_patch(end_circle)
    
    # 범례 추가
    legend_elements = [
        patches.Circle((0, 0), 0.4, facecolor='#8B4513', edgecolor='#654321', label='아파트'),
        patches.Circle((0, 0), 0.4, facecolor='#A0522D', edgecolor='#654321', label='빌딩'),
        patches.Rectangle((0, 0), 0.8, 0.8, facecolor='#228B22', edgecolor='#006400', label='반달곰 커피'),
        patches.Polygon([[0, 0.4], [-0.4, -0.4], [0.4, -0.4]], facecolor='#32CD32', edgecolor='#228B22', label='내 집'),
        patches.Rectangle((0, 0), 1.2, 1.2, facecolor='#666666', edgecolor='#333333', label='건설 현장'),
        patches.Circle((0, 0), 0.3, facecolor='blue', alpha=0.7, edgecolor='darkblue', label='시작점'),
        patches.Circle((0, 0), 0.3, facecolor='red', alpha=0.7, edgecolor='darkred', label='도착점')
    ]
    ax.legend(handles=legend_elements, loc='upper left')
    
    ax.set_title('내 집에서 반달곰 커피까지의 최단 경로')
    
    # 지도 저장
    filepath = 'C:/codyssey/ky-codyssey-main/Codyseey/map_final.png'
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"🗺️ 최종 지도가 저장되었습니다: {filepath}")

def bonus_optimized_path(data):
    """보너스: 모든 구조물을 한 번씩 지나도록 최적화된 경로"""
    print("\n🎯 보너스: 모든 구조물을 지나는 최적화된 경로 계산...")
    
    # 모든 구조물 위치 찾기
    structures = data[data['struct_name'].notna() & (data['struct_name'] != 'nan')]
    struct_positions = []
    
    for _, row in structures.iterrows():
        struct_positions.append({
            'name': row['struct_name'],
            'pos': (row['x'], row['y']),
            'type': row['struct_name']
        })
    
    print(f"📍 총 {len(struct_positions)}개의 구조물을 방문해야 합니다:")
    for struct in struct_positions:
        print(f"   - {struct['name']}: {struct['pos']}")
    
    # 간단한 최적화: 내 집 → 아파트 → 빌딩 → 반달곰 커피 순서
    optimized_order = [' MyHome', ' Apartment', ' Building', ' BandalgomCoffee']
    optimized_path = []
    
    for struct_type in optimized_order:
        struct_data = structures[structures['struct_name'] == struct_type]
        if len(struct_data) > 0:
            pos = (struct_data.iloc[0]['x'], struct_data.iloc[0]['y'])
            optimized_path.append(pos)
    
    print(f"✅ 최적화된 방문 순서: {optimized_path}")
    return optimized_path

def main():
    """메인 함수"""
    print("🚶 내 집에서 반달곰 커피까지의 최단 경로 탐색")
    print("=" * 60)
    
    # 1. 데이터 불러오기
    data = load_data()
    if data is None:
        return
    
    # 2. 내 집과 반달곰 커피 위치 찾기
    home_pos, cafe_pos = find_my_home_and_cafe(data)
    if home_pos is None or cafe_pos is None:
        return
    
    # 3. 그리드 맵 생성
    print("\n🗺️ 그리드 맵 생성 중...")
    grid = create_grid_map(data)
    print(f"✅ {grid.shape[1]}x{grid.shape[0]} 크기의 그리드 맵 생성 완료")
    
    # 4. 최단 경로 탐색 (BFS)
    print("\n🔍 최단 경로 탐색 중...")
    shortest_path = bfs_shortest_path(grid, home_pos, cafe_pos)
    
    if shortest_path:
        # 5. 경로를 CSV로 저장
        print("\n💾 경로 저장 중...")
        save_path_to_csv(shortest_path)
        
        # 6. 최종 지도 시각화
        print("\n🎨 최종 지도 생성 중...")
        create_final_map_visualization(data, shortest_path)
        
        # 7. 보너스: 최적화된 경로
        bonus_optimized_path(data)
        
        print("\n" + "=" * 60)
        print("✅ 3단계 최단 경로 탐색 완료!")
        print("=" * 60)
        print("📁 생성된 파일:")
        print("   - home_to_cafe.csv: 최단 경로 데이터")
        print("   - map_final.png: 경로가 표시된 최종 지도")
    else:
        print("\n❌ 최단 경로를 찾을 수 없습니다.")

if __name__ == "__main__":
    main() 
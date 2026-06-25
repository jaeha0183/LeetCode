class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 줄이 1개면 지그재그가 안 생김 → 원본 그대로 리턴
        # (이게 없으면 아래에서 row가 범위 밖으로 나가 터짐)
        if numRows == 1:
            return s
        
        # 줄 개수만큼 빈 버킷 생성. 예: numRows=3 이면 [[], [], []]
        # 각 글자가 자기가 속한 줄 버킷에 들어감
        rows = [[] for _ in range(numRows)]
        
        # row = 현재 줄 번호(0부터), step = 이동 방향(+1=내려감, -1=올라감)
        row, step = 0, 1
        
        for ch in s:
            rows[row].append(ch)   # 현재 글자를 지금 줄 버킷에 담기
            
            if row == 0:           # 맨 위 줄 → 이제 내려가야 함
                step = 1
            elif row == numRows - 1:  # 맨 아래 줄 → 이제 올라가야 함
                step = -1
            # 중간 줄이면 둘 다 해당 안 됨 → 방향 그대로 유지
            
            row += step            # 다음 줄로 이동
        
        # 각 버킷을 문자열로 합치고(안쪽 join), 줄 순서대로 이어붙임(바깥 join)
        return ''.join(''.join(r) for r in rows)
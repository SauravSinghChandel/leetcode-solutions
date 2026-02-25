class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:

        seen_points = []

        parallel_count = defaultdict(int)
        collinear_count = defaultdict(int)

        parallel_side_count = defaultdict(int)
        collinear_side_count = defaultdict(int)

        res = 0
        rhombus_twice = 0

        for x1, y1 in points:
            for x2, y2 in seen_points:
                dx = x1 - x2
                dy = y1 - y2

                if dx == 0:
                    k = float('inf')
                    b = x1

                else:
                    k = dy/dx
                    b = y1 - k * x1

                    k = round(k, 8)
                    b = round(b, 8)

                slope_id = k
                line_id = (k, b)

                res += parallel_count[slope_id] - collinear_count[line_id]

                parallel_count[slope_id] += 1
                collinear_count[line_id] += 1

                side_len = dx * dx + dy * dy

                rhombus_twice += parallel_side_count[(k, side_len)] - collinear_side_count[(k, b, side_len)]

                parallel_side_count[(k, side_len)] += 1
                collinear_side_count[(k, b, side_len)] += 1

            seen_points.append((x1, y1))

        return res - rhombus_twice // 2

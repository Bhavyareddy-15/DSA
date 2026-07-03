def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        count = 0
        result = []

        while i >= 0 or j >= 0 or count:
            total = count

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            count = total // 2

        return "".join(result[::-1])

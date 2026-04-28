class StackList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,url):
        self.items.append(url)

    def pop(self):
        if self.is_empty():
            return 'Riwayat Kosong'
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return 'Riwayat Kosong'
        return self.items[-1]
    
    def size(self):
        return len(self.items)

print('=== Stack dengan Class ===')
s1 = StackList()
s1.push('www.google.com')
s1.push('www.facebook.com')
s1.push('www.youtube.com')
s1.push('www.instagram.com')
print('Riwayat Navigasi Browser: ', s1.items)
print('Riwayat dihapus:', s1.pop())
print('Lihat Riwayat Teratas:', s1.peek())
print('Ukuran Riwayat:', s1.size())
print('Apakah Riwayat Kosong?', s1.is_empty())
print('Riwayat Navigasi Browser setelah pop: ', s1.items)

class ItemInfo:
    def __init__(self, href, title, text) -> None:
        self.href = href
        self.title = title
        self.text = text
    
    def __str__(self) -> str:
        return f'title: {self.title} / text: {self.text} / href: {self.href}'
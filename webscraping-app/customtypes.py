class ItemInfo:
    def __init__(self, href, title, text) -> None:
        self.href = href
        self.title = title
        self.text = text
    
    def __str__(self) -> str:
        return f'title: {self.title} / text: {self.text} / href: {self.href}'

class PlayerInfo:
    def __init__(self, name='', position='', number='-', age='', team='', nationality='', height='', 
        foot='', joined='', signed_from='', contract='', market_value='') -> None:
        self.name = name
        self.position = position
        self.number = number
        self.age = age
        self.team = team
        self.nationality = nationality
        self.height = height
        self.foot = foot
        self.joined = joined
        self.signed_from = signed_from
        self.contract = contract
        self.market_value = market_value

    def __str__(self) -> str:
        return f'Nome: {self.name} / Time: {self.team} / Posição: {self.position}'
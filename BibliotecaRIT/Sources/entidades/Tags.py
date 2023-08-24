from BibliotecaRIT.Sources.enums.EnumTag import EnumTag


class Tags:
    def __init__(self):
        self._tags = [None for i in range(len(EnumTag))]
    
    def addTag(self,tag:EnumTag):
        if tag is not None:
            if self._tags[tag.value] is None:
                self._tags[tag.value] = tag
    
    def toString(self)->str:
        string = ""
        for tag in self._tags:
            if tag is not None:
                string += tag.name + "\n"
        return string

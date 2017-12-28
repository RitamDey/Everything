def make_book(num_pages):
    pages = [(1,),]
    count = 1

    while count < num_pages:
        if count+2 <= num_pages:
            pages.append((count+1, count+2))
            count += 2
        elif count+1 <= num_pages:
            pages.append((count+1,))
            count += 1
    return pages


def turn_count(pages, page_key):
    for page in pages:
        if page_key in page:
            return pages.index(page)


if __name__ == '__main__':
    pages = make_book(int(input()))
    to_find = int(input())

    print(min(turn_count(pages, to_find), turn_count(pages[::-1], to_find)))

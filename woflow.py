import requests
import collections


def bfs(start: str, endpoint: str) -> tuple[str, int]:
    # track frequency of visits
    frequency = {}

    # prevent duplicate visits
    seen = set()

    # bfs frontier
    queue = collections.deque()
    queue.append(start)
    frequency[start] = 1
    seen.add(start)

    while len(queue) != 0:
        # bfs - invoke the endpoint from frontier while q has nodes
        node = queue.popleft()

        # construct url
        url = f'{endpoint}{node}'

        # invoke endpoint, fetch children from json 
        children = requests.get(url).json()[0]["child_node_ids"]

        for child in children:
            if child not in seen:
                # append new child to frontier, start freq counter at 1
                queue.append(child)
                frequency[child] = 1
                seen.add(child)
            else:
                # increment freq counter for existing child
                frequency[child] += 1

    return max(frequency, key=frequency.get), len(seen)

       
if __name__ == '__main__':
    common, unique = bfs(
        '089ef556-dfff-4ff2-9733-654645be56fe', 
        'https://nodes-on-nodes-challenge.herokuapp.com/nodes/'
    )

    print(f'Number of unique nodes: {unique}')
    print(f'Most common node: {common}')
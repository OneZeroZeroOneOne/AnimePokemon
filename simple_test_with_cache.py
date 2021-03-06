import asyncio
from PokemonModel import *

async def main():
    b = PokemonFetch()

    start_time = time.time()
    pok_count = 0
    pok = await b.get_pokemon_id(25)

    print(pok.ToString())
    print("\n\n!!!форми покездона:")
    for i in await pok.GetForms():
        print(i.ToString())

    pok_evol = await pok.GetEvolutions()
    print("\n\n!!!еволить из:")
    for i in pok_evol['from']:
        print(i)

    print("\n\n!!!еволить в:")
    for i in pok_evol['into']:
        print(i)
    print("Времени понадобилось для первого вызова {}\nВсего покемонов создано {}".format(time.time() - start_time, pok_count))

    start_time = time.time()
    pok = await b.get_pokemon_id(3)

    print(pok)
    print("\n\n!!!форми покездона:")
    for i in await pok.GetForms():
        print(i)

    pok_evol = await pok.GetEvolutions()
    print("\n\n!!!еволить из:")
    for i in pok_evol['from']:
        print(i)

    print("\n\n!!!еволить в:")
    for i in pok_evol['into']:
        print(i)
    print("Времени понадобилось для второго вызова {}\nВсего покемонов создано {}".format(time.time() - start_time, pok_count))

    '''
    pok = await PokemonFetch.get_pokemon_id(100)
    await pok.GetEvolutions()
    print(pok.ToString())
    pok = await PokemonFetch.get_pokemon_id(150)
    await pok.GetEvolutions()
    print(pok.ToString())
    print("Времени понадобилось для первого вызова {}\nВсего покемонов создано {}".format(time.time() - start_time, pok_count))
    '''
    '''start_time = time.time()
    pokes = await PokemonFetch.get_pokemon_list(1)
    for i in pokes:
        print(i)
    print("Времени понадобилось для второго вызова {}".format(time.time() - start_time))
    start_time = time.time()
    pokes = await PokemonFetch.get_pokemon_list(1)
    for i in pokes:
        print(i)
    print("Времени понадобилось для третьего вызова {}".format(time.time() - start_time))'''

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

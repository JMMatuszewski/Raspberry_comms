from udp_factory import UDPFactory
from tcp_factory import TCPFactory

#Client
def main():

    TCP = TCPFactory()
    UDP = UDPFactory()
    #TCP = TCPFactory()
    #UDP = UDPFactory()

    TCPsocket = TCP.create_socket()
    TCPaddress = TCP.create_address()

    UDPsocket = UDP.create_socket()
    UDPaddress = UDP.create_address()

    print(f'TCP: {TCPsocket.__class__.__name__}')
    print(f'TCP: {TCPaddress.__class__.__name__}')

    print(f'TCP: {UDPsocket.__class__.__name__}')
    print(f'TCP: {UDPaddress.__class__.__name__}')

if __name__ == "__main__":
    main()


# class RaspberryComms:
#     def __init__(self) -> None:
#         print("First blood")

# if __name__ == "__main__":
#     RaspberryComms()
#     socket = UDPFactory()

#     print(socket)

    # country = Country.ENGLAND
    # factory = InternationalProvider.create(country)
    # language = factory.create_language()
    # capital_city = factory.create_capital()

    # print(f'Country: {country.name}')
    # print(f'Language: {language.__class__.__name__}')
    # print(f'Greet: {language.greet()}')
    # print(f'Capital: {capital_city.__class__.__name__}')
    # print(f'Population: {capital_city.get_population()}')
    # print(f'Attractions: {capital_city.list_top_attractions()}')

# HostIpConfigIpV6AddressConfigTypeEnum

This specifies how the ipv6 address is configured for the interface.  We follow rfc4293 in defining the values for the configType.  Possible values: - `other`: Any other type of address configuration other than the below   mentioned ones will fall under this category.      For e.g., automatic   address configuration for the link local address falls under   this type. - `manual`: The address is configured manually. - `dhcp`: The address is configured through dhcp. - `linklayer`: The address is obtained through stateless autoconfiguration. - `random`: The address is chosen by the system at random   e.g., an IPv4 address within 169.254/16, or an RFC   3041 privacy address.    ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



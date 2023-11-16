# HostInternetScsiHbaIscsiIpv6Address

The IPv6 address.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | IPv6 address.  ***Since:*** vSphere API 6.0  | 
**prefix_length** | **int** | IPv6 address prefix length.  ***Since:*** vSphere API 6.0  | 
**origin** | **str** | Type of the address.  See { @Vim::Host::HostBusAdapter::IscsiIpv6Address::AddressConfigurationType }. Note: While setting IPv6 address, value of origin should be set to static.  ***Since:*** vSphere API 6.0  | 
**operation** | **str** | Operation to be performed with the IP address.  See { @Vim::Host::HostBusAdapter::IscsiIpv6Address::IPv6AddressOperation }. Note: This field/operation is used only while setting the IPProperties on host bus adapter. This field would not have any value (Unset) while viewing IPProperties of the host bus adapter.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.host_internet_scsi_hba_iscsi_ipv6_address import HostInternetScsiHbaIscsiIpv6Address

# TODO update the JSON string below
json = "{}"
# create an instance of HostInternetScsiHbaIscsiIpv6Address from a JSON string
host_internet_scsi_hba_iscsi_ipv6_address_instance = HostInternetScsiHbaIscsiIpv6Address.from_json(json)
# print the JSON string representation of the object
print HostInternetScsiHbaIscsiIpv6Address.to_json()

# convert the object into a dict
host_internet_scsi_hba_iscsi_ipv6_address_dict = host_internet_scsi_hba_iscsi_ipv6_address_instance.to_dict()
# create an instance of HostInternetScsiHbaIscsiIpv6Address from a dict
host_internet_scsi_hba_iscsi_ipv6_address_form_dict = host_internet_scsi_hba_iscsi_ipv6_address.from_dict(host_internet_scsi_hba_iscsi_ipv6_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



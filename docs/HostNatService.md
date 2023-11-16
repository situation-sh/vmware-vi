# HostNatService

A network address translation (NAT) service instance provides firewall and network address translation services for a virtual network.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The instance ID of the NAT service.  ***Since:*** VI API 2.5  | 
**spec** | [**HostNatServiceSpec**](HostNatServiceSpec.md) |  | 

## Example

```python
from vmware_vi.models.host_nat_service import HostNatService

# TODO update the JSON string below
json = "{}"
# create an instance of HostNatService from a JSON string
host_nat_service_instance = HostNatService.from_json(json)
# print the JSON string representation of the object
print HostNatService.to_json()

# convert the object into a dict
host_nat_service_dict = host_nat_service_instance.to_dict()
# create an instance of HostNatService from a dict
host_nat_service_form_dict = host_nat_service.from_dict(host_nat_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FindByDnsNameRequestType

The parameters of *SearchIndex.FindByDnsName*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**dns_name** | **str** | The fully qualified domain name to find.  | 
**vm_search** | **bool** | if true, search for virtual machines, otherwise search for hosts.  | 

## Example

```python
from vmware_vi.models.find_by_dns_name_request_type import FindByDnsNameRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of FindByDnsNameRequestType from a JSON string
find_by_dns_name_request_type_instance = FindByDnsNameRequestType.from_json(json)
# print the JSON string representation of the object
print FindByDnsNameRequestType.to_json()

# convert the object into a dict
find_by_dns_name_request_type_dict = find_by_dns_name_request_type_instance.to_dict()
# create an instance of FindByDnsNameRequestType from a dict
find_by_dns_name_request_type_form_dict = find_by_dns_name_request_type.from_dict(find_by_dns_name_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



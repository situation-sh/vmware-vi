# FindAllByDnsNameRequestType

The parameters of *SearchIndex.FindAllByDnsName*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**dns_name** | **str** | The fully qualified domain name to find.  | 
**vm_search** | **bool** | If true, search for virtual machines, otherwise search for hosts.  | 

## Example

```python
from vmware_vi.models.find_all_by_dns_name_request_type import FindAllByDnsNameRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of FindAllByDnsNameRequestType from a JSON string
find_all_by_dns_name_request_type_instance = FindAllByDnsNameRequestType.from_json(json)
# print the JSON string representation of the object
print FindAllByDnsNameRequestType.to_json()

# convert the object into a dict
find_all_by_dns_name_request_type_dict = find_all_by_dns_name_request_type_instance.to_dict()
# create an instance of FindAllByDnsNameRequestType from a dict
find_all_by_dns_name_request_type_form_dict = find_all_by_dns_name_request_type.from_dict(find_all_by_dns_name_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



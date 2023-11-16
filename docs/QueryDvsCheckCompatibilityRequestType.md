# QueryDvsCheckCompatibilityRequestType

The parameters of *DistributedVirtualSwitchManager.QueryDvsCheckCompatibility*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_container** | [**DistributedVirtualSwitchManagerHostContainer**](DistributedVirtualSwitchManagerHostContainer.md) |  | 
**dvs_product_spec** | [**DistributedVirtualSwitchManagerDvsProductSpec**](DistributedVirtualSwitchManagerDvsProductSpec.md) |  | [optional] 
**host_filter_spec** | [**List[DistributedVirtualSwitchManagerHostDvsFilterSpec]**](DistributedVirtualSwitchManagerHostDvsFilterSpec.md) | The hosts against which to check compatibility. This is a filterSpec and users can use this to specify all hosts in a container (datacenter, folder, or computeResource), an array of hosts, or hosts that might or might not be a DVS member.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.query_dvs_check_compatibility_request_type import QueryDvsCheckCompatibilityRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDvsCheckCompatibilityRequestType from a JSON string
query_dvs_check_compatibility_request_type_instance = QueryDvsCheckCompatibilityRequestType.from_json(json)
# print the JSON string representation of the object
print QueryDvsCheckCompatibilityRequestType.to_json()

# convert the object into a dict
query_dvs_check_compatibility_request_type_dict = query_dvs_check_compatibility_request_type_instance.to_dict()
# create an instance of QueryDvsCheckCompatibilityRequestType from a dict
query_dvs_check_compatibility_request_type_form_dict = query_dvs_check_compatibility_request_type.from_dict(query_dvs_check_compatibility_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



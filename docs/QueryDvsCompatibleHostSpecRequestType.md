# QueryDvsCompatibleHostSpecRequestType

The parameters of *DistributedVirtualSwitchManager.QueryDvsCompatibleHostSpec*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_product_spec** | [**DistributedVirtualSwitchProductSpec**](DistributedVirtualSwitchProductSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_dvs_compatible_host_spec_request_type import QueryDvsCompatibleHostSpecRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDvsCompatibleHostSpecRequestType from a JSON string
query_dvs_compatible_host_spec_request_type_instance = QueryDvsCompatibleHostSpecRequestType.from_json(json)
# print the JSON string representation of the object
print QueryDvsCompatibleHostSpecRequestType.to_json()

# convert the object into a dict
query_dvs_compatible_host_spec_request_type_dict = query_dvs_compatible_host_spec_request_type_instance.to_dict()
# create an instance of QueryDvsCompatibleHostSpecRequestType from a dict
query_dvs_compatible_host_spec_request_type_form_dict = query_dvs_compatible_host_spec_request_type.from_dict(query_dvs_compatible_host_spec_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



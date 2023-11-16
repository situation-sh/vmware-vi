# DiscoverFcoeHbasRequestType

The parameters of *HostStorageSystem.DiscoverFcoeHbas*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fcoe_spec** | [**FcoeConfigFcoeSpecification**](FcoeConfigFcoeSpecification.md) |  | 

## Example

```python
from vmware_vi.models.discover_fcoe_hbas_request_type import DiscoverFcoeHbasRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoverFcoeHbasRequestType from a JSON string
discover_fcoe_hbas_request_type_instance = DiscoverFcoeHbasRequestType.from_json(json)
# print the JSON string representation of the object
print DiscoverFcoeHbasRequestType.to_json()

# convert the object into a dict
discover_fcoe_hbas_request_type_dict = discover_fcoe_hbas_request_type_instance.to_dict()
# create an instance of DiscoverFcoeHbasRequestType from a dict
discover_fcoe_hbas_request_type_form_dict = discover_fcoe_hbas_request_type.from_dict(discover_fcoe_hbas_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



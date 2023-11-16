# FetchDVPortKeysRequestType

The parameters of *DistributedVirtualSwitch.FetchDVPortKeys*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria** | [**DistributedVirtualSwitchPortCriteria**](DistributedVirtualSwitchPortCriteria.md) |  | [optional] 

## Example

```python
from vmware_vi.models.fetch_dv_port_keys_request_type import FetchDVPortKeysRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of FetchDVPortKeysRequestType from a JSON string
fetch_dv_port_keys_request_type_instance = FetchDVPortKeysRequestType.from_json(json)
# print the JSON string representation of the object
print FetchDVPortKeysRequestType.to_json()

# convert the object into a dict
fetch_dv_port_keys_request_type_dict = fetch_dv_port_keys_request_type_instance.to_dict()
# create an instance of FetchDVPortKeysRequestType from a dict
fetch_dv_port_keys_request_type_form_dict = fetch_dv_port_keys_request_type.from_dict(fetch_dv_port_keys_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



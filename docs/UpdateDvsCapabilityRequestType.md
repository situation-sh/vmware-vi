# UpdateDvsCapabilityRequestType

The parameters of *DistributedVirtualSwitch.UpdateDvsCapability*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capability** | [**DVSCapability**](DVSCapability.md) |  | 

## Example

```python
from vmware_vi.models.update_dvs_capability_request_type import UpdateDvsCapabilityRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDvsCapabilityRequestType from a JSON string
update_dvs_capability_request_type_instance = UpdateDvsCapabilityRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateDvsCapabilityRequestType.to_json()

# convert the object into a dict
update_dvs_capability_request_type_dict = update_dvs_capability_request_type_instance.to_dict()
# create an instance of UpdateDvsCapabilityRequestType from a dict
update_dvs_capability_request_type_form_dict = update_dvs_capability_request_type.from_dict(update_dvs_capability_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



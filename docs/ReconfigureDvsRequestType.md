# ReconfigureDvsRequestType

The parameters of *DistributedVirtualSwitch.ReconfigureDvs_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**DVSConfigSpec**](DVSConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.reconfigure_dvs_request_type import ReconfigureDvsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReconfigureDvsRequestType from a JSON string
reconfigure_dvs_request_type_instance = ReconfigureDvsRequestType.from_json(json)
# print the JSON string representation of the object
print ReconfigureDvsRequestType.to_json()

# convert the object into a dict
reconfigure_dvs_request_type_dict = reconfigure_dvs_request_type_instance.to_dict()
# create an instance of ReconfigureDvsRequestType from a dict
reconfigure_dvs_request_type_form_dict = reconfigure_dvs_request_type.from_dict(reconfigure_dvs_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



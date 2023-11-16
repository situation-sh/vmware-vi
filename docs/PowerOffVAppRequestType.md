# PowerOffVAppRequestType

The parameters of *VirtualApp.PowerOffVApp_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** | If force is false, the shutdown order in the vApp is executed. If force is true, all virtual machines are powered-off (regardless of shutdown order).  | 

## Example

```python
from vmware_vi.models.power_off_v_app_request_type import PowerOffVAppRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of PowerOffVAppRequestType from a JSON string
power_off_v_app_request_type_instance = PowerOffVAppRequestType.from_json(json)
# print the JSON string representation of the object
print PowerOffVAppRequestType.to_json()

# convert the object into a dict
power_off_v_app_request_type_dict = power_off_v_app_request_type_instance.to_dict()
# create an instance of PowerOffVAppRequestType from a dict
power_off_v_app_request_type_form_dict = power_off_v_app_request_type.from_dict(power_off_v_app_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



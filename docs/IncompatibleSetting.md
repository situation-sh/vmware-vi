# IncompatibleSetting

Thrown when two parameters in the customization settings conflict with each other.  For example, a client may not specify both a Workgroup and a DomainName. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflicting_property** | **str** | The name of the setting that is conflicting.  | 

## Example

```python
from vmware_vi.models.incompatible_setting import IncompatibleSetting

# TODO update the JSON string below
json = "{}"
# create an instance of IncompatibleSetting from a JSON string
incompatible_setting_instance = IncompatibleSetting.from_json(json)
# print the JSON string representation of the object
print IncompatibleSetting.to_json()

# convert the object into a dict
incompatible_setting_dict = incompatible_setting_instance.to_dict()
# create an instance of IncompatibleSetting from a dict
incompatible_setting_form_dict = incompatible_setting.from_dict(incompatible_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



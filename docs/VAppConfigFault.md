# VAppConfigFault

Base for configuration / environment issues that can be thrown when powering on or changing the configuration of a vApp.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.v_app_config_fault import VAppConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of VAppConfigFault from a JSON string
v_app_config_fault_instance = VAppConfigFault.from_json(json)
# print the JSON string representation of the object
print VAppConfigFault.to_json()

# convert the object into a dict
v_app_config_fault_dict = v_app_config_fault_instance.to_dict()
# create an instance of VAppConfigFault from a dict
v_app_config_fault_form_dict = v_app_config_fault.from_dict(v_app_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# VAppPropertyFault

The base fault for all vApp property configuration issues  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The fully-qualified id of the property, including instance and class identifiers.  ***Since:*** vSphere API 4.0  | 
**category** | **str** | The user-readable category  ***Since:*** vSphere API 4.0  | 
**label** | **str** | The user-readable label  ***Since:*** vSphere API 4.0  | 
**type** | **str** | The type specified for the property  ***Since:*** vSphere API 4.0  | 
**value** | **str** | The value of the property  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.v_app_property_fault import VAppPropertyFault

# TODO update the JSON string below
json = "{}"
# create an instance of VAppPropertyFault from a JSON string
v_app_property_fault_instance = VAppPropertyFault.from_json(json)
# print the JSON string representation of the object
print VAppPropertyFault.to_json()

# convert the object into a dict
v_app_property_fault_dict = v_app_property_fault_instance.to_dict()
# create an instance of VAppPropertyFault from a dict
v_app_property_fault_form_dict = v_app_property_fault.from_dict(v_app_property_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



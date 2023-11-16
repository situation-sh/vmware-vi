# HealthUpdateInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier provided by the HealthUpdateProvider.  Identifiers are required to be unique per HealthUpdateProvider.  ***Since:*** vSphere API 6.5  | 
**component_type** | **str** | The component type.  For supported values, see *HealthUpdateInfoComponentType_enum*  ***Since:*** vSphere API 6.5  | 
**description** | **str** | A description of the change in health.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.health_update_info import HealthUpdateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HealthUpdateInfo from a JSON string
health_update_info_instance = HealthUpdateInfo.from_json(json)
# print the JSON string representation of the object
print HealthUpdateInfo.to_json()

# convert the object into a dict
health_update_info_dict = health_update_info_instance.to_dict()
# create an instance of HealthUpdateInfo from a dict
health_update_info_form_dict = health_update_info.from_dict(health_update_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



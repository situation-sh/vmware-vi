# HealthUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**health_update_info_id** | **str** | The ID of the corresponding HealthUpdateInfo.  ***Since:*** vSphere API 6.5  | 
**id** | **str** | The ID of this particular HealthUpdate instance, for cross-reference with HealthUpdateProvider logs.  ***Since:*** vSphere API 6.5  | 
**status** | [**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md) |  | 
**remediation** | **str** | A description of the physical remediation required to resolve this health update.  For example, \&quot;Replace Fan #3\&quot;.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.health_update import HealthUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of HealthUpdate from a JSON string
health_update_instance = HealthUpdate.from_json(json)
# print the JSON string representation of the object
print HealthUpdate.to_json()

# convert the object into a dict
health_update_dict = health_update_instance.to_dict()
# create an instance of HealthUpdate from a dict
health_update_form_dict = health_update.from_dict(health_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



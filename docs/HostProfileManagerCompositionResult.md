# HostProfileManagerCompositionResult

The data class for host profile composition result.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[LocalizableMessage]**](LocalizableMessage.md) | The composition errors for all targets, for example, the source profile doesn&#39;t exist.  ***Since:*** vSphere API 6.5  | [optional] 
**results** | [**List[HostProfileManagerCompositionResultResultElement]**](HostProfileManagerCompositionResultResultElement.md) | The array of *HostProfileManagerCompositionResultResultElement* for all the target host profiles.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.host_profile_manager_composition_result import HostProfileManagerCompositionResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostProfileManagerCompositionResult from a JSON string
host_profile_manager_composition_result_instance = HostProfileManagerCompositionResult.from_json(json)
# print the JSON string representation of the object
print HostProfileManagerCompositionResult.to_json()

# convert the object into a dict
host_profile_manager_composition_result_dict = host_profile_manager_composition_result_instance.to_dict()
# create an instance of HostProfileManagerCompositionResult from a dict
host_profile_manager_composition_result_form_dict = host_profile_manager_composition_result.from_dict(host_profile_manager_composition_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



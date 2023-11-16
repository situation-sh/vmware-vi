# HostProfileManagerCompositionResultResultElement

Composition result for a specific target host profile.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**status** | **str** | The composition status.  See *HostProfileManagerCompositionResultResultElementStatus_enum* for details of supported values.  ***Since:*** vSphere API 6.5  | 
**errors** | [**List[LocalizableMessage]**](LocalizableMessage.md) | The composition errors.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.host_profile_manager_composition_result_result_element import HostProfileManagerCompositionResultResultElement

# TODO update the JSON string below
json = "{}"
# create an instance of HostProfileManagerCompositionResultResultElement from a JSON string
host_profile_manager_composition_result_result_element_instance = HostProfileManagerCompositionResultResultElement.from_json(json)
# print the JSON string representation of the object
print HostProfileManagerCompositionResultResultElement.to_json()

# convert the object into a dict
host_profile_manager_composition_result_result_element_dict = host_profile_manager_composition_result_result_element_instance.to_dict()
# create an instance of HostProfileManagerCompositionResultResultElement from a dict
host_profile_manager_composition_result_result_element_form_dict = host_profile_manager_composition_result_result_element.from_dict(host_profile_manager_composition_result_result_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



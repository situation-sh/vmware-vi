# ProfileApplyProfileElement

DataObject which represents an ApplyProfile element.  An ApplyProfile element is an ApplyProfile for a set of host configuration settings which may be instanced. For example, there may be multiple virtual switch instances represented by individual ApplyProfileElement DataObjects.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The linkable identifier.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.profile_apply_profile_element import ProfileApplyProfileElement

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileApplyProfileElement from a JSON string
profile_apply_profile_element_instance = ProfileApplyProfileElement.from_json(json)
# print the JSON string representation of the object
print ProfileApplyProfileElement.to_json()

# convert the object into a dict
profile_apply_profile_element_dict = profile_apply_profile_element_instance.to_dict()
# create an instance of ProfileApplyProfileElement from a dict
profile_apply_profile_element_form_dict = profile_apply_profile_element.from_dict(profile_apply_profile_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



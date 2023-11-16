# ArrayOfDVSContactInfo

A boxed array of *DVSContactInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSContactInfo]**](DVSContactInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_contact_info import ArrayOfDVSContactInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSContactInfo from a JSON string
array_of_dvs_contact_info_instance = ArrayOfDVSContactInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSContactInfo.to_json()

# convert the object into a dict
array_of_dvs_contact_info_dict = array_of_dvs_contact_info_instance.to_dict()
# create an instance of ArrayOfDVSContactInfo from a dict
array_of_dvs_contact_info_form_dict = array_of_dvs_contact_info.from_dict(array_of_dvs_contact_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



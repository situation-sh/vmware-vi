# ArrayOfLicenseEvent

A boxed array of *LicenseEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LicenseEvent]**](LicenseEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_license_event import ArrayOfLicenseEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLicenseEvent from a JSON string
array_of_license_event_instance = ArrayOfLicenseEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfLicenseEvent.to_json()

# convert the object into a dict
array_of_license_event_dict = array_of_license_event_instance.to_dict()
# create an instance of ArrayOfLicenseEvent from a dict
array_of_license_event_form_dict = array_of_license_event.from_dict(array_of_license_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



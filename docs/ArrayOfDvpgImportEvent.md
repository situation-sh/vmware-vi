# ArrayOfDvpgImportEvent

A boxed array of *DvpgImportEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvpgImportEvent]**](DvpgImportEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvpg_import_event import ArrayOfDvpgImportEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvpgImportEvent from a JSON string
array_of_dvpg_import_event_instance = ArrayOfDvpgImportEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvpgImportEvent.to_json()

# convert the object into a dict
array_of_dvpg_import_event_dict = array_of_dvpg_import_event_instance.to_dict()
# create an instance of ArrayOfDvpgImportEvent from a dict
array_of_dvpg_import_event_form_dict = array_of_dvpg_import_event.from_dict(array_of_dvpg_import_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



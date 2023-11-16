# DVSSelection

Class to specify selection criteria of vSphere Distributed Switch.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dvs_uuid** | **str** | vSphere Distributed Switch uuid  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.dvs_selection import DVSSelection

# TODO update the JSON string below
json = "{}"
# create an instance of DVSSelection from a JSON string
dvs_selection_instance = DVSSelection.from_json(json)
# print the JSON string representation of the object
print DVSSelection.to_json()

# convert the object into a dict
dvs_selection_dict = dvs_selection_instance.to_dict()
# create an instance of DVSSelection from a dict
dvs_selection_form_dict = dvs_selection.from_dict(dvs_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



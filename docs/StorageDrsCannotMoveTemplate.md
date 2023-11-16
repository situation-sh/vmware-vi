# StorageDrsCannotMoveTemplate

This fault is thrown because Storage DRS cannot generate recommendations to relocate template VMs across datastores.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.storage_drs_cannot_move_template import StorageDrsCannotMoveTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsCannotMoveTemplate from a JSON string
storage_drs_cannot_move_template_instance = StorageDrsCannotMoveTemplate.from_json(json)
# print the JSON string representation of the object
print StorageDrsCannotMoveTemplate.to_json()

# convert the object into a dict
storage_drs_cannot_move_template_dict = storage_drs_cannot_move_template_instance.to_dict()
# create an instance of StorageDrsCannotMoveTemplate from a dict
storage_drs_cannot_move_template_form_dict = storage_drs_cannot_move_template.from_dict(storage_drs_cannot_move_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateVvolDatastoreRequestType

The parameters of *HostDatastoreSystem.CreateVvolDatastore*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HostDatastoreSystemVvolDatastoreSpec**](HostDatastoreSystemVvolDatastoreSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_vvol_datastore_request_type import CreateVvolDatastoreRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVvolDatastoreRequestType from a JSON string
create_vvol_datastore_request_type_instance = CreateVvolDatastoreRequestType.from_json(json)
# print the JSON string representation of the object
print CreateVvolDatastoreRequestType.to_json()

# convert the object into a dict
create_vvol_datastore_request_type_dict = create_vvol_datastore_request_type_instance.to_dict()
# create an instance of CreateVvolDatastoreRequestType from a dict
create_vvol_datastore_request_type_form_dict = create_vvol_datastore_request_type.from_dict(create_vvol_datastore_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



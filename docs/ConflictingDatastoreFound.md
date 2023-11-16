# ConflictingDatastoreFound

ConflictingDatastoreFound is thrown when the conflicting datastores with the same url but backed by different disks are found in the host and the target datacenter.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the datastore.  ***Since:*** vSphere API 5.1  | 
**url** | **str** | The unique locator for the datastore.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.conflicting_datastore_found import ConflictingDatastoreFound

# TODO update the JSON string below
json = "{}"
# create an instance of ConflictingDatastoreFound from a JSON string
conflicting_datastore_found_instance = ConflictingDatastoreFound.from_json(json)
# print the JSON string representation of the object
print ConflictingDatastoreFound.to_json()

# convert the object into a dict
conflicting_datastore_found_dict = conflicting_datastore_found_instance.to_dict()
# create an instance of ConflictingDatastoreFound from a dict
conflicting_datastore_found_form_dict = conflicting_datastore_found.from_dict(conflicting_datastore_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



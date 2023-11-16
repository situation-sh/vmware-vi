# HostDatastoreBrowserSearchResults

This data object type contains the results of a search method for one datastore.  A search method typically returns a set of these objects as an array. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**folder_path** | **str** | Relative path to the top-level folder.  | [optional] 
**file** | [**List[FileInfo]**](FileInfo.md) | Set of matching files, if any.  | [optional] 

## Example

```python
from vmware_vi.models.host_datastore_browser_search_results import HostDatastoreBrowserSearchResults

# TODO update the JSON string below
json = "{}"
# create an instance of HostDatastoreBrowserSearchResults from a JSON string
host_datastore_browser_search_results_instance = HostDatastoreBrowserSearchResults.from_json(json)
# print the JSON string representation of the object
print HostDatastoreBrowserSearchResults.to_json()

# convert the object into a dict
host_datastore_browser_search_results_dict = host_datastore_browser_search_results_instance.to_dict()
# create an instance of HostDatastoreBrowserSearchResults from a dict
host_datastore_browser_search_results_form_dict = host_datastore_browser_search_results.from_dict(host_datastore_browser_search_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



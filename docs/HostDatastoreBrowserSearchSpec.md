# HostDatastoreBrowserSearchSpec

The data object type describes a search for files in one or more datastores.  The properties do not include the starting datastore path because that path is a separate parameter to the search method.  A SearchSpec contains the query parameters and some global search modifiers. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**List[FileQuery]**](FileQuery.md) | The set of file types to match, search criteria specific to the file type, and the amount of detail for a file.  These search parameters are specific to a file type, meaning that they can be specified only if the file type to which they are associated is in the set. A file type cannot appear more than once in the set.  If this query object is not present, then all files providing only file level details are matched.  | [optional] 
**details** | [**FileQueryFlags**](FileQueryFlags.md) |  | [optional] 
**search_case_insensitive** | **bool** | This flag indicates whether or not to search using a case insensitive match on type.  In general the algorithm used to match file types relies on file extensions. Although the specific file extensions used are encapsulated by this API, clients are still allowed to modify the filtering behavior.  By default, the DatastoreBrowser uses a platform-consistent algorithm to determine if a file is of a type. Specifically on Linux, where case is important, the search is case sensitive. On Windows, case is not important, so the search is case insensitive.  In an environment with heterogenous platforms, being platform-consistent may not be desirable. As a result, the default behavior can be overridden by setting this optional flag.  | [optional] 
**match_pattern** | **List[str]** | Specifies a list of file patterns that must match for a file to be returned.  This search property is a filter that applies globally so that only files matching the specified patterns are returned, regardless of the other search parameters.  | [optional] 
**sort_folders_first** | **bool** | By default, files are sorted in alphabetical order regardless of file type.  If this flag is set to \&quot;true\&quot;, folders are placed at the start of the list of results in alphabetical order. The remaining files follow in alphabetical order.  | [optional] 

## Example

```python
from vmware_vi.models.host_datastore_browser_search_spec import HostDatastoreBrowserSearchSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostDatastoreBrowserSearchSpec from a JSON string
host_datastore_browser_search_spec_instance = HostDatastoreBrowserSearchSpec.from_json(json)
# print the JSON string representation of the object
print HostDatastoreBrowserSearchSpec.to_json()

# convert the object into a dict
host_datastore_browser_search_spec_dict = host_datastore_browser_search_spec_instance.to_dict()
# create an instance of HostDatastoreBrowserSearchSpec from a dict
host_datastore_browser_search_spec_form_dict = host_datastore_browser_search_spec.from_dict(host_datastore_browser_search_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



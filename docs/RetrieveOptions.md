# RetrieveOptions

Options for *PropertyCollector.RetrievePropertiesEx*.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_objects** | **int** | The maximum number of *ObjectContent* data objects that should be returned in a single result from *PropertyCollector.RetrievePropertiesEx*.  An unset value indicates that there is no maximum. In this case *PropertyCollector* policy may still limit the number of objects. Any remaining objects may be retrieved with *PropertyCollector.ContinueRetrievePropertiesEx*.  A positive value causes *PropertyCollector.RetrievePropertiesEx* to suspend the retrieval when the count of objects reaches the specified maximum. *PropertyCollector* policy may still limit the count to something less than *RetrieveOptions.maxObjects*. Any remaining objects may be retrieved with *PropertyCollector.ContinueRetrievePropertiesEx*.  A value less than or equal to 0 is illegal.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.retrieve_options import RetrieveOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveOptions from a JSON string
retrieve_options_instance = RetrieveOptions.from_json(json)
# print the JSON string representation of the object
print RetrieveOptions.to_json()

# convert the object into a dict
retrieve_options_dict = retrieve_options_instance.to_dict()
# create an instance of RetrieveOptions from a dict
retrieve_options_form_dict = retrieve_options.from_dict(retrieve_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



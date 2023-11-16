# RetrieveResult

Result of *PropertyCollector.RetrievePropertiesEx* and *PropertyCollector.ContinueRetrievePropertiesEx*  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | A token used to retrieve further retrieve results.  If set, the token should be passed to *PropertyCollector.ContinueRetrievePropertiesEx* to retrieve more results. Each token may be passed to continueRetrievePropertiesEx only once, and only in the same session in which it was returned and to the same *PropertyCollector* object that returned it.  If unset, there are no further results to retrieve after this *RetrieveResult*.  ***Since:*** vSphere API 4.1  | [optional] 
**objects** | [**List[ObjectContent]**](ObjectContent.md) | retrieved objects.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.retrieve_result import RetrieveResult

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveResult from a JSON string
retrieve_result_instance = RetrieveResult.from_json(json)
# print the JSON string representation of the object
print RetrieveResult.to_json()

# convert the object into a dict
retrieve_result_dict = retrieve_result_instance.to_dict()
# create an instance of RetrieveResult from a dict
retrieve_result_form_dict = retrieve_result.from_dict(retrieve_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



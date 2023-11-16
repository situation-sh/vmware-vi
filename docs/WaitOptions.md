# WaitOptions

Options for *PropertyCollector.WaitForUpdatesEx*.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_wait_seconds** | **int** | The number of seconds the *PropertyCollector* should wait before returning null.  Returning updates may take longer if the actual calculation time exceeds *WaitOptions.maxWaitSeconds*. Additionally *PropertyCollector* policy may cause it to return null sooner than *WaitOptions.maxWaitSeconds*.  An unset value causes *PropertyCollector.WaitForUpdatesEx* to wait as long as possible for updates. Policy may still cause the *PropertyCollector* to return null at some point.  A value of 0 causes *PropertyCollector.WaitForUpdatesEx* to do one update calculation and return any results. This behavior is similar to *PropertyCollector.CheckForUpdates*.  A positive value causes *PropertyCollector.WaitForUpdatesEx* to return null if no updates are available within the specified number of seconds. The choice of a positive value often depends on the client communication stack. For example it may be helpful to choose a duration shorter than a local HTTP request timeout. Typically it should be no shorter than a few minutes.  A negative value is illegal.  ***Since:*** vSphere API 4.1  | [optional] 
**max_object_updates** | **int** | The maximum number of *ObjectUpdate* entries that should be returned in a single result from *PropertyCollector.WaitForUpdatesEx*.  See *UpdateSet.truncated*  An unset value indicates that there is no maximum. In this case *PropertyCollector* policy may still limit the number of objects that appear in an *UpdateSet*.  A positive value causes *PropertyCollector.WaitForUpdatesEx* to suspend the update calculation when the total count of *ObjectUpdate* entries ready to return reaches the specified maximum. *PropertyCollector* policy may still limit the total count to something less than *WaitOptions.maxObjectUpdates*.  A value less than or equal to 0 is illegal.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.wait_options import WaitOptions

# TODO update the JSON string below
json = "{}"
# create an instance of WaitOptions from a JSON string
wait_options_instance = WaitOptions.from_json(json)
# print the JSON string representation of the object
print WaitOptions.to_json()

# convert the object into a dict
wait_options_dict = wait_options_instance.to_dict()
# create an instance of WaitOptions from a dict
wait_options_form_dict = wait_options.from_dict(wait_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



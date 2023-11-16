# UpdateSet

A set of updates that represent the changes since a prior call to *PropertyCollector.CheckForUpdates*, *PropertyCollector.WaitForUpdates*, or *PropertyCollector.WaitForUpdatesEx*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | New data version to pass in the next call to *PropertyCollector.CheckForUpdates*, *PropertyCollector.WaitForUpdates*, or *PropertyCollector.WaitForUpdatesEx*.  These versions, although they are opaque, are strongly ordered in the sense that passing a version to *PropertyCollector.WaitForUpdates*, *PropertyCollector.CheckForUpdates* or *PropertyCollector.WaitForUpdatesEx* requests updates that reflect changes in the objects selected by the Filter that happened after the specified version.  | 
**filter_set** | [**List[PropertyFilterUpdate]**](PropertyFilterUpdate.md) | Set of managed object updates detected by specific filters.  Updates are reported in sets. Each set is associated with a reference to a filter that detected the updates in the set.  | [optional] 
**truncated** | **bool** | If true, this *UpdateSet* contains results from a suspended change calculation, which places restrictions on the use of version.  The *PropertyCollector* may suspend a calculation due to server policy or if the total number of *ObjectUpdate* entries summed across every *PropertyFilterUpdate* reached the maximum specified in *WaitOptions.maxObjectUpdates*. The client can pass the \&quot;truncated data version\&quot; to *PropertyCollector.WaitForUpdatesEx* to resume the update calculation, which will start on the filter where it left off. A truncated data version cannot be used more than once and may not be passed to *PropertyCollector.CheckForUpdates* or *PropertyCollector.WaitForUpdates*. *UpdateSet.truncated* will never be true in an *UpdateSet* returned from *PropertyCollector.CheckForUpdates* or *PropertyCollector.WaitForUpdates*.  If false, this *UpdateSet* contains a complete change calculation or the last part of a series of suspended change calculations. The version may be passed to *PropertyCollector.CheckForUpdates*, *PropertyCollector.WaitForUpdates*, or *PropertyCollector.WaitForUpdatesEx* more than once. Re-using a version allows a client to recover a change sequence after a transient failure on a previous call.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.update_set import UpdateSet

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSet from a JSON string
update_set_instance = UpdateSet.from_json(json)
# print the JSON string representation of the object
print UpdateSet.to_json()

# convert the object into a dict
update_set_dict = update_set_instance.to_dict()
# create an instance of UpdateSet from a dict
update_set_form_dict = update_set.from_dict(update_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SwapDatastoreNotWritableOnHost

The compute resource and/or virtual machine configurations indicate that when executing on the host the virtual machine should use a specific datastore, but host does not have read/write access to that datastore.  (It may have no access at all, or read-only access.) If executing on the host the virtual machine would instead use its own directory for swapfile placement. This is a compatibility warning, not an error.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.swap_datastore_not_writable_on_host import SwapDatastoreNotWritableOnHost

# TODO update the JSON string below
json = "{}"
# create an instance of SwapDatastoreNotWritableOnHost from a JSON string
swap_datastore_not_writable_on_host_instance = SwapDatastoreNotWritableOnHost.from_json(json)
# print the JSON string representation of the object
print SwapDatastoreNotWritableOnHost.to_json()

# convert the object into a dict
swap_datastore_not_writable_on_host_dict = swap_datastore_not_writable_on_host_instance.to_dict()
# create an instance of SwapDatastoreNotWritableOnHost from a dict
swap_datastore_not_writable_on_host_form_dict = swap_datastore_not_writable_on_host.from_dict(swap_datastore_not_writable_on_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



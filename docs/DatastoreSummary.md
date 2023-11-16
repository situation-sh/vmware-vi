# DatastoreSummary

Summary information about the datastore.  The status fields and managed object reference is not set when an object of this type is created. These fields and references are typically set later when these objects are associated with a host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**name** | **str** | The name of the datastore.  | 
**url** | **str** | The unique locator for the datastore.  This property is guaranteed to be valid only if *DatastoreSummary.accessible* is true.  | 
**capacity** | **int** | Maximum capacity of this datastore, in bytes.  This value is updated periodically by the server. It can be explicitly refreshed with the Refresh operation. This property is guaranteed to be valid only if *DatastoreSummary.accessible* is true.  | 
**free_space** | **int** | Available space of this datastore, in bytes.  The server periodically updates this value. It can be explicitly refreshed with the Refresh operation. This property is guaranteed to be valid only if *DatastoreSummary.accessible* is true.  | 
**uncommitted** | **int** | Total additional storage space, in bytes, potentially used by all virtual machines on this datastore.  The server periodically updates this value. It can be explicitly refreshed with the *Datastore.RefreshDatastoreStorageInfo* operation. This property is valid only if *DatastoreSummary.accessible* is true.  ***Since:*** vSphere API 4.0  | [optional] 
**accessible** | **bool** | The connectivity status of this datastore.  If this is set to false, meaning the datastore is not accessible, this datastore&#39;s capacity and freespace properties cannot be validated. Furthermore, if this property is set to false, some of the properties in this summary and in *DatastoreInfo* should not be used. Refer to the documentation for the property of your interest. For datastores accessed from multiple hosts, vCenter Server reports *DatastoreSummary.accessible* as an aggregated value of the properties reported in *HostMountInfo*. For instance, if a datastore is accessible through a subset of hosts, then the value of *DatastoreSummary.accessible* will be reported as true by vCenter Server. And the reason for a daastore being inaccessible from a host will be reported in *HostMountInfo.inaccessibleReason*  | 
**multiple_host_access** | **bool** | More than one host in the datacenter has been configured with access to the datastore.  This is only provided by VirtualCenter.  | [optional] 
**type** | **str** | Type of file system volume, such as VMFS or NFS.  See also *HostFileSystemVolume.type*.  | 
**maintenance_mode** | **str** | The current maintenance mode state of the datastore.  The set of possible values is described in *DatastoreSummaryMaintenanceModeState_enum*.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.datastore_summary import DatastoreSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreSummary from a JSON string
datastore_summary_instance = DatastoreSummary.from_json(json)
# print the JSON string representation of the object
print DatastoreSummary.to_json()

# convert the object into a dict
datastore_summary_dict = datastore_summary_instance.to_dict()
# create an instance of DatastoreSummary from a dict
datastore_summary_form_dict = datastore_summary.from_dict(datastore_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



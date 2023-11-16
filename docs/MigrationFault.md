# MigrationFault

Base object type for issues that can occur when reassigning the execution host of a virtual machine using migrate or relocate.  These issues are typically used as argument in the MigrationEvent. When a MigrationFault is used as a value in a MigrationEvent, the type of MigrationEvent determines if the issue is a warning or an error (for example, MigrationHostWarningEvent or MigrationHostErrorEvent). When thrown as an exception, the fault is an error.  Issues are categorized as errors or warnings according to the following criteria:  If the virtual machine is powered on: 1. Error for fatal problems with the VMotion interfaces or licensing. 2. Error if VMotion would fail. 3. Error if VMotion would in any way interrupt the continuous and consistent    operation of the virtual machine. 4. Warning for potential performance or connectivity problems between the    source and destination VMotion interfaces. 5. Warning if the virtual machine's currently disconnected devices may not    be connectable after VMotion.     If the virtual machine is powered off or suspended: 1. Error if the destination host cannot access all the files that comprise    the virtual machine (including virtual disks). 2. Error if aspects of the virtual machine are not supported by the    destination host's hardware or software. 3. Warning if problems would occur when powering on or resuming the    virtual machine, if the usage/configuration of the destination    host were to remain in its current state. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.migration_fault import MigrationFault

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationFault from a JSON string
migration_fault_instance = MigrationFault.from_json(json)
# print the JSON string representation of the object
print MigrationFault.to_json()

# convert the object into a dict
migration_fault_dict = migration_fault_instance.to_dict()
# create an instance of MigrationFault from a dict
migration_fault_form_dict = migration_fault.from_dict(migration_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



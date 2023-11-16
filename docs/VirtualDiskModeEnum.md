# VirtualDiskModeEnum

The list of known disk modes.  The list of supported disk modes varies by the backing type. The \"persistent\" mode is supported by every backing type.  Possible values: - `persistent`: Changes are immediately and permanently written to the virtual disk. - `nonpersistent`: Changes to virtual disk are made to a redo log and discarded at power off. - `undoable`: Changes are made to a redo log, but you are given the option to commit or undo. - `independent_persistent`: Same as persistent, but not affected by snapshots. - `independent_nonpersistent`: Same as nonpersistent, but not affected by snapshots. - `append`: Changes are appended to the redo log; you revoke changes by removing the undo log. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



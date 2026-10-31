package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An MFT record facet is a grouping of characteristics unique to the details of a single file as managed in an NTFS (new technology filesystem) master file table (which is a collection of information about all files on an NTFS filesystem). [based on https://docs.microsoft.com/en-us/windows/win32/devnotes/master-file-table]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MftRecordFacet extends Facet {

  private Integer mftFileID;
  private ZonedDateTime mftFileNameAccessedTime;
  private ZonedDateTime mftFileNameCreatedTime;
  private Integer mftFileNameLength;
  private ZonedDateTime mftFileNameModifiedTime;
  private ZonedDateTime mftFileNameRecordChangeTime;
  private Integer mftFlags;
  private Integer mftParentID;
  private ZonedDateTime mftRecordChangeTime;
  private Integer ntfsHardLinkCount;
  private String ntfsOwnerID;
  private String ntfsOwnerSID;


}
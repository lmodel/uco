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
  A snapshot is a file system object representing a snapshot of the contents of a part of a file system at a point in time.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Snapshot extends FileSystemObject {



}
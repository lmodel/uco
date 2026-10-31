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
  A socket is a special file used for inter-process communication, which enables communication between two processes. In addition to sending data, processes can send file descriptors across a Unix domain socket connection using the sendmsg() and recvmsg() system calls. Unlike named pipes which allow only unidirectional data flow, sockets are fully duplex-capable. [based on https://en.wikipedia.org/wiki/Unix_file_types]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Socket extends FileSystemObject {



}
import Link from 'next/link';
import styles from '../../styles/Navbar.module.css';

const Navbar = () => {
  return (
    <nav className={styles.navbar}>
      <div className={styles.logo}>
        <Link href="/">
          <a>WebApp</a>
        </Link>
      </div>
      <ul className={styles.navLinks}>
        <li>
          <Link href="/">
            <a>Home</a>
          </Link>
        </li>
        {/* Add additional navigation links as needed */}
      </ul>
    </nav>
  );
};

export default Navbar;
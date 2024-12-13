import styles from '../../styles/Home.module.css';

const Footer = () => {
  return (
    <footer className={styles.footer}>
      <p>&copy; {new Date().getFullYear()} - Web App</p>
    </footer>
  );
};

export default Footer;